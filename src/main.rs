#[tokio::main]
async fn main() -> anyhow::Result<()> {
    kubrick::app::runtime::run().await
}
