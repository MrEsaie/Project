Sub ExportDashboardToPDF()
    Dim ws As Worksheet
    Dim pdfPath As String
    Dim fileName As String

    ' Define worksheet and file path
    Set ws = ThisWorkbook.Sheets("Executive Dashboard")
    pdfPath = ThisWorkbook.Path & "\"
    fileName = "Financial_Summary_" & Format(Now(), "YYYYMMDD") & ".pdf"

    ' Export sheet to PDF
    ws.ExportAsFixedFormat _
        Type:=xlTypePDF, _
        fileName:=pdfPath & fileName, _
        Quality:=xlQualityStandard, _
        IncludeDocProperties:=True, _
        IgnorePrintAreas:=False, _
        OpenAfterPublish:=False

    MsgBox "Financial Dashboard successfully exported to PDF!", vbInformation, "Export Complete"
End Sub
