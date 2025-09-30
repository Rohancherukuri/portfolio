import reflex as rx

config = rx.Config(
    app_name="portfolio",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)