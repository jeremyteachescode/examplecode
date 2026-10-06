"""Builds the CSE Form 5 Quarterly Listing Statement package for Avanti Gold Corp. (AVNT)."""
from dataclasses import dataclass
from datetime import date

CSE_FORM5_DEADLINE_DAYS = 60  # days after quarter end


@dataclass
class QuarterlyFiling:
    issuer: str
    ticker: str
    period_end: date
    private_placement_proceeds: float
    finders_fees: float
    exploration_spend: float


def filing_due_date(period_end: date) -> date:
    from datetime import timedelta
    return period_end + timedelta(days=CSE_FORM5_DEADLINE_DAYS)


def build_schedule_b(filing: QuarterlyFiling) -> dict:
    """Schedule B: securities issued and use of proceeds."""
    return {
        "issuer": filing.issuer,
        "ticker": filing.ticker,
        "securities_issued": {
            "type": "Private placement (Form 9 notice filed)",
            "gross_proceeds": filing.private_placement_proceeds,
            "finders_fees": filing.finders_fees,
        },
        "exploration_expenditures": filing.exploration_spend,
    }


if __name__ == "__main__":
    q3 = QuarterlyFiling("Avanti Gold Corp.", "AVNT", date(2026, 9, 30), 5_000_000, 240_000, 1_850_000)
    print("Form 5 due:", filing_due_date(q3.period_end))
    print(build_schedule_b(q3))
