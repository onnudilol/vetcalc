from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse

from treatment_sheets.forms import TxSheetForm, TxItemForm
from treatment_sheets.models import TxSheet, TxItem

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Flowable

from io import BytesIO
from datetime import date

User = get_user_model()


def treatment_sheets(request):
    return render(request, 'tx_sheet/tx_sheet.html', {'navbar': 'tx_sheet'})


@login_required()
def view_treatment_sheet(request, sheet_id):

    sheet = get_object_or_404(TxSheet, id=sheet_id)

    form = TxItemForm()

    if request.user == sheet.owner:

        if request.method == 'POST':
            form = TxItemForm(data=request.POST)

            if form.is_valid():
                tx_sheet = form.save(sheet=sheet)
                return redirect(tx_sheet)

        return render(request, 'tx_sheet/tx_sheet_view.html', {'navbar': 'tx_sheet', 'sheet': sheet, 'form': form})

    else:
        raise PermissionDenied


@login_required()
def new_tx_sheet(request):
    sheet_form = TxSheetForm()
    item_form = TxItemForm()

    if request.method == 'POST':
        sheet_form = TxSheetForm(data=request.POST)
        item_form = TxItemForm(data=request.POST)

        if sheet_form.is_valid() and item_form.is_valid():
            tx_sheet = sheet_form.save(owner=request.user)
            item_form.save(sheet=tx_sheet)
            return redirect(tx_sheet)

    return render(request, 'tx_sheet/tx_sheet_new.html', {'navbar': 'tx_sheet',
                                                          'sheet_form': sheet_form, 'item_form': item_form})


@login_required()
def del_item_tx_sheet(request, sheet_id, item_id):
    tx_sheet = get_object_or_404(TxSheet, id=sheet_id)

    if request.user == tx_sheet.owner:
        TxItem.objects.get(id=item_id).delete()
        return redirect(tx_sheet)

    else:
        raise PermissionDenied


@login_required()
def edit_tx_sheet(request, sheet_id):
    tx_sheet = get_object_or_404(TxSheet, id=sheet_id)
    form = TxSheetForm(instance=tx_sheet)

    if request.user == tx_sheet.owner:

        if request.method == 'POST':
            form = TxSheetForm(data=request.POST)

            if form.is_valid():
                defaults = {'owner': request.user,
                            'name': request.POST['name'],
                            'comment': request.POST['comment'],
                            'date': date.today()}
                tx_sheet = form.update(sheet_id=sheet_id, defaults=defaults)
                return redirect(tx_sheet)

        return render(request, 'tx_sheet/tx_sheet_edit.html', {'navbar': 'tx_sheet', 'form': form})

    else:
        raise PermissionDenied


@login_required()
def output_pdf(request, sheet_id):

    class Line(Flowable):

        def __init__(self, width, height=0):
            Flowable.__init__(self)
            self.width = width
            self.height = height

        def __repr__(self):
            return "Line(w={})".format(self.width)

        def draw(self):
            self.canv.line(0, self.height, self.width, self.height)

    sheet = TxSheet.objects.get(id=sheet_id)

    if request.user == sheet.owner:

        filename = '{}_{}.pdf'.format(sheet.name, sheet.date)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        buffer = BytesIO()

        story = list()
        doc = SimpleDocTemplate(filename=buffer, pagesize=letter, rightMargin=50, leftMargin=50,
                                topMargin=50, bottomMargin=50)
        styles = getSampleStyleSheet()
        p = ParagraphStyle('LeftIndented')
        p.leftIndent = 24
        styles.add(p)

        ptext = '<font size=36>{}</font>'.format(sheet.name)
        story.append(Paragraph(ptext, styles["Normal"]))
        story.append(Spacer(1, 0.6 * inch))

        line = Line(500)
        story.append(line)
        story.append(Spacer(1, 0.2 * inch))

        ptext = '<font size=10>Date: {}</font>'.format(sheet.date)
        story.append(Paragraph(ptext, styles["Normal"]))
        story.append(Spacer(1, 0.2 * inch))

        comment = sheet.comment.split('\n')

        for line in comment:

            ptext = '<font size=10>{}</font>'.format(line)
            story.append(Paragraph(ptext, styles["Normal"]))
            story.append(Spacer(0, 5))

        story.append(Spacer(1, 0.2 * inch))

        for item in sheet.txitem_set.all():
            ptext = '<font size=14>{}</font>'.format(item.med.name)
            story.append(Paragraph(ptext, styles["Normal"]))
            story.append(Spacer(1, 0.2 * inch))

            ptext = '<font size=10>{}</font>'.format(item.instruction)
            story.append(Paragraph(ptext, styles["LeftIndented"]))
            story.append(Spacer(1, 0.1 * inch))

            ptext = '<font size=10>{}</font>'.format(item.med.desc)
            story.append(Paragraph(ptext, styles["LeftIndented"]))
            story.append(Spacer(1, 0.2 * inch))

        doc.build(story)
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)

        return response

    else:
        raise PermissionDenied
