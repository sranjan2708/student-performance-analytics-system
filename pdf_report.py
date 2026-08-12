from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)


def create_pdf_report(
    output_path,
    overall_statistics,
    subject_statistics,
    student_records
):

    # ==========================================
    # Create PDF Document
    # ==========================================

    document = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=30,
        leftMargin=30,
        topMargin=30,
        bottomMargin=30
    )


    # ==========================================
    # Styles
    # ==========================================

    styles = getSampleStyleSheet()

    title_style = styles["Title"]

    heading_style = styles["Heading2"]

    normal_style = styles["Normal"]


    # ==========================================
    # PDF Content
    # ==========================================

    elements = []


    # ==========================================
    # Report Title
    # ==========================================

    elements.append(
        Paragraph(
            "Student Performance Analytics Report",
            title_style
        )
    )

    elements.append(
        Spacer(1, 20)
    )


    # ==========================================
    # Overall Statistics
    # ==========================================

    elements.append(
        Paragraph(
            "Overall Statistics",
            heading_style
        )
    )

    elements.append(
        Spacer(1, 10)
    )


    overall_data = [
        ["Metric", "Value"],

        [
            "Total Students",
            overall_statistics["total_students"]
        ],

        [
            "Passed Students",
            overall_statistics["pass_count"]
        ],

        [
            "Failed Students",
            overall_statistics["fail_count"]
        ],

        [
            "Overall Average",
            overall_statistics["overall_average"]
        ],

        [
            "Highest Score",
            overall_statistics["highest_total"]
        ],

        [
            "Lowest Score",
            overall_statistics["lowest_total"]
        ],

        [
            "Topper",
            overall_statistics["topper"]
        ]
    ]


    overall_table = Table(
        overall_data,
        colWidths=[250, 200]
    )


    overall_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.HexColor("#1f4e79")
            ),

            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.white
            ),

            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "Helvetica-Bold"
            ),

            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.grey
            ),

            (
                "PADDING",
                (0, 0),
                (-1, -1),
                8
            )
        ])
    )


    elements.append(overall_table)

    elements.append(
        Spacer(1, 25)
    )


    # ==========================================
    # Subject Statistics
    # ==========================================

    elements.append(
        Paragraph(
            "Subject Statistics",
            heading_style
        )
    )

    elements.append(
        Spacer(1, 10)
    )


    subject_data = [
        [
            "Subject",
            "Average",
            "Highest",
            "Lowest"
        ]
    ]


    for subject, stats in subject_statistics.items():

        subject_data.append([
            subject,
            stats["average"],
            stats["highest"],
            stats["lowest"]
        ])


    subject_table = Table(
        subject_data,
        colWidths=[150, 100, 100, 100]
    )


    subject_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.HexColor("#1f4e79")
            ),

            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.white
            ),

            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "Helvetica-Bold"
            ),

            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.grey
            ),

            (
                "PADDING",
                (0, 0),
                (-1, -1),
                8
            )
        ])
    )


    elements.append(subject_table)

    elements.append(
        Spacer(1, 25)
    )


    # ==========================================
    # Student Records
    # ==========================================

    elements.append(
        Paragraph(
            "Student Records",
            heading_style
        )
    )

    elements.append(
        Spacer(1, 10)
    )


    student_data = [
        [
            "Name",
            "Math",
            "Science",
            "English",
            "Total",
            "Average",
            "Result"
        ]
    ]


    for student in student_records:

        student_data.append([
            student["Name"],
            student["Math"],
            student["Science"],
            student["English"],
            student["Total"],
            student["Average"],
            student["Result"]
        ])


    student_table = Table(
        student_data,
        repeatRows=1
    )


    student_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.HexColor("#1f4e79")
            ),

            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.white
            ),

            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "Helvetica-Bold"
            ),

            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.grey
            ),

            (
                "FONTSIZE",
                (0, 0),
                (-1, -1),
                7
            ),

            (
                "PADDING",
                (0, 0),
                (-1, -1),
                5
            )
        ])
    )


    elements.append(student_table)


    # ==========================================
    # Build PDF
    # ==========================================

    document.build(elements)