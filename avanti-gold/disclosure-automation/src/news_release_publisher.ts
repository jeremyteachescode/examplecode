// Publishes Avanti Gold (AVNT) news releases to the CSE issuer portal and Slack #avanti-gold-ir.
import axios from "axios";

interface NewsRelease {
  ticker: "AVNT";
  headline: string;
  body: string;
  materialChange: boolean;
}

export async function publishRelease(release: NewsRelease): Promise<void> {
  if (release.materialChange) {
    // Notify CSE Market Surveillance before release per timely disclosure policy
    await axios.post(`${process.env.CSE_PORTAL_URL}/surveillance/pre-notice`, {
      ticker: release.ticker,
      headline: release.headline,
    });
  }

  await axios.post(`${process.env.CSE_PORTAL_URL}/filings/news-release`, release);

  await axios.post(process.env.SLACK_WEBHOOK_URL!, {
    text: `:newspaper: AVNT release published: ${release.headline}`,
  });
}

publishRelease({
  ticker: "AVNT",
  headline: "Avanti Gold announces C$5M private placement",
  body: "Avanti Gold Corp. (CSE: AVNT) announces a non-brokered private placement...",
  materialChange: true,
}).catch(console.error);
