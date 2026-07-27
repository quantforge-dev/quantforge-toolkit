"""
Report Builder.
"""


class ReportBuilder:

    """
    Convert analysis
    results into reports.
    """

    def __init__(
        self,
        analysis,
    ):

        self.analysis = analysis

    def build(self):

        report = []

        for key, value in self.analysis.items():

            report.append(
                f"{key}: {value}"
            )

        return "\n".join(report)
