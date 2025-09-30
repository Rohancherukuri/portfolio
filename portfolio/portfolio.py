import os
import datetime
import reflex as rx

# --- Color Palette ---
COLORS = {
    "bg_primary": "#0A0A0A",
    "bg_secondary": "#1A1A1A",
    "bg_card": "#141414",
    "text_primary": "#FFFFFF",
    "text_secondary": "#A0A0A0",
    "accent": "#6366F1",
    "accent_hover": "#818CF8",
    "border": "#2A2A2A",
    "gradient_start": "#6366F1",
    "gradient_end": "#8B5CF6",
}

# --- Gradient Keyframes ---
ANIMATIONS = {
    "gradientShift": {
        "0%": {"background-position": "0% 50%"},
        "50%": {"background-position": "100% 50%"},
        "100%": {"background-position": "0% 50%"},
    },
    "fadeInUp": {
        "0%": {"opacity": 0, "transform": "translateY(20px)"},
        "100%": {"opacity": 1, "transform": "translateY(0)"},
    },
}

# --- Pre-built Components ---
def styled_link(text: str, url: str, icon: str = None) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.cond(icon, rx.icon(icon, size=18)),
            rx.text(text, font_size="0.95rem", font_weight="500"),
            spacing="2",
            align="center",
        ),
        href=url,
        is_external=True,
        color=COLORS["text_secondary"],
        text_decoration="none",
        transition="all 0.3s ease",
        _hover={
            "color": COLORS["accent"],
            "transform": "translateY(-3px) scale(1.05)",
            "text_shadow": f"0 0 12px {COLORS['accent']}50",
        },
    )

def gradient_text(text: str, size: str = "3rem") -> rx.Component:
    return rx.heading(
        text,
        font_size=size,
        font_weight="800",
        background_image=f"linear-gradient(270deg, {COLORS['gradient_start']}, {COLORS['gradient_end']}, {COLORS['gradient_start']})",
        background_size="400% 400%",
        background_clip="text",
        color="transparent",
        margin_bottom="0.5rem",
        animation="gradientShift 8s ease infinite",
    )

# --- Section Heading ---
def section_heading(title: str) -> rx.Component:
    return rx.vstack(
        gradient_text(title, "2rem"),
        rx.box(
            height="3px",
            width="60px",
            background=f"linear-gradient(90deg, {COLORS['gradient_start']}, {COLORS['gradient_end']})",
            border_radius="full",
        ),
        spacing="3",
        margin_bottom="2rem",
    )

# --- Header ---
def header() -> rx.Component:
    return rx.vstack(
        rx.box(
            position="absolute",
            top="0",
            left="0",
            right="0",
            height="350px",
            background=f"radial-gradient(circle at top, {COLORS['gradient_start']}33, transparent 70%)",
            animation="gradientShift 20s ease infinite",
            background_size="200% 200%",
            z_index="-1",
        ),
        rx.hstack(
            rx.vstack(
                gradient_text("Rohan Cherukuri", "2.8rem"),
                rx.text(
                    "Machine Learning Engineer",
                    font_size="1.25rem",
                    color=COLORS["text_secondary"],
                    font_weight="500",
                    margin_bottom="1rem",
                ),
                rx.vstack(
                    rx.hstack(
                        rx.icon("map-pin", size=16, color=COLORS["text_secondary"]),
                        rx.text("Hyderabad, India", color=COLORS["text_secondary"], font_size="0.95rem"),
                        spacing="2",
                    ),
                    rx.hstack(
                        rx.icon("mail", size=16, color=COLORS["text_secondary"]),
                        rx.text("rohanoxob3000@gmail.com", color=COLORS["text_secondary"], font_size="0.95rem"),
                        spacing="2",
                    ),
                    rx.hstack(
                        rx.icon("phone", size=16, color=COLORS["text_secondary"]),
                        rx.text("7032675528", color=COLORS["text_secondary"], font_size="0.95rem"),
                        spacing="2",
                    ),
                    spacing="3",
                    align_items="start",
                ),
                rx.hstack(
                    styled_link("GitHub", "https://github.com/Rohancherukuri", "github"),
                    styled_link("LinkedIn", "https://www.linkedin.com/in/rohan-cherukuri-5877b2182", "linkedin"),
                    spacing="4",
                    padding_top="1rem",
                ),
                align_items="start",
                spacing="3",
                animation="fadeInUp 1s ease forwards",
            ),
            rx.spacer(),
            rx.box(
                # rx.avatar(
                #     name="Rohan Cherukuri",
                #     size="9",
                #     src="/profile.jpg",
                #     radius="full",
                #     border=f"3px solid {COLORS['accent']}",
                # ),
                position="relative",
                _before={
                    "content": '""',
                    "position": "absolute",
                    "inset": "-6px",
                    "border_radius": "50%",
                    "background": f"linear-gradient(135deg, {COLORS['gradient_start']}, {COLORS['gradient_end']})",
                    "animation": "gradientShift 6s ease infinite",
                    "background_size": "300% 300%",
                    "z_index": "-1",
                },
                transition="transform 0.3s ease",
                _hover={"transform": "scale(1.05)"},
            ),
            align="center",
            width="100%",
            padding_bottom="2rem",
        ),
        width="100%",
        position="relative",
        padding_top="3rem",
    )

# --- About Section ---
def about_me() -> rx.Component:
    return rx.vstack(
        section_heading("About Me"),
        rx.box(
            rx.text(
                "As a Machine Learning Engineer, I specialize in developing and deploying scalable ML solutions across computer vision, NLP, and statistical modeling. Experienced in taking projects from concept to production.",
                font_size="1.1rem",
                color=COLORS["text_secondary"],
                line_height="1.8",
                text_align="justify",
            ),
            padding="2rem",
            background=COLORS["bg_card"],
            border_radius="12px",
            border=f"1px solid {COLORS['border']}",
            transition="all 0.3s ease",
            _hover={
                "border_color": COLORS["accent"],
                "box_shadow": f"0 0 20px {COLORS['accent']}20",
            },
        ),
        width="100%",
        padding_y="3rem",
    )

# --- Experience Section ---
def experience_item(company, role, date_range, description):
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.heading(role, font_size="1.3rem", font_weight="600", color=COLORS["text_primary"]),
                rx.spacer(),
                rx.badge(date_range, color_scheme="gray", variant="soft", padding="0.5rem 1rem"),
            ),
            rx.text(company, font_size="1.1rem", color=COLORS["accent"], font_weight="500"),
            rx.text(description, font_size="1rem", color=COLORS["text_secondary"], line_height="1.7"),
            spacing="3",
        ),
        padding="1.5rem",
        background=COLORS["bg_card"],
        border=f"1px solid {COLORS['border']}",
        border_radius="12px",
        transition="all 0.3s ease",
        _hover={"transform": "translateX(8px)", "border_color": COLORS["accent"]},
    )

def experience():
    return rx.vstack(
        section_heading("Work Experience"),
        rx.vstack(
            experience_item(
                "Archimydes",
                "Machine Learning Engineer",
                "Jan 2024 - Feb 2025",
                "Built and deployed scalable cross-platform apps for patient ECG analysis with AI-driven diagnostics."
            ),
            experience_item(
                "Star Health And Allied Insurance Limited",
                "Deputy Manager - Analytics",
                "Jul 2022 - Aug 2023",
                "Delivered ML, NLP, and analytics projects that improved operational efficiency and customer insights."
            ),
            experience_item(
                "iNeuron",
                "Machine Learning Intern",
                "May 2021 - Nov 2021",
                "Developed a class-based custom clustering algorithm with logging and ML pipeline experience."
            ),
            spacing="4",
        ),
        width="100%",
        padding_y="3rem",
    )

# --- Projects Section ---
def project_card(title, description, tech_stack, link=None):
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.heading(title, font_size="1.3rem", font_weight="600", color=COLORS["text_primary"]),
                rx.spacer(),
                rx.cond(link, rx.link(rx.icon("external-link", size=20, color=COLORS["accent"]), href=link, is_external=True)),
            ),
            rx.text(description, font_size="0.95rem", color=COLORS["text_secondary"], line_height="1.6"),
            rx.flex(
                *[rx.badge(tech, variant="soft", color_scheme="purple", padding="0.3rem 0.8rem") for tech in tech_stack.split(", ")],
                wrap="wrap",
                gap="3",
                spacing="3"
            ),
            spacing="3",
        ),
        padding="1.5rem",
        background=COLORS["bg_card"],
        border=f"1px solid {COLORS['border']}",
        border_radius="12px",
        transition="all 0.3s ease",
        _hover={"transform": "translateY(-4px)", "border_color": COLORS["accent"], "box_shadow": f"0 10px 30px {COLORS['accent']}20"},
    )

def projects():
    return rx.vstack(
        section_heading("Featured Projects"),
        rx.grid(
            project_card("3D Image Reconstruction", "Neural radiance fields for 3D reconstruction.", "Python, PyTorch, NeRF"),
            project_card("Speech To Text Analysis", "Advanced speech recognition with diarization.", "PyTorch, Whisper, Pydub"),
            project_card("Industry Alerts Web App", "Real-time automated customer alerts app.", "Python, Flet, OracleDB"),
            project_card("AI ECG Analysis Tools", "Automated ECG validation and reporting pipeline.", "Python, Deep Learning, WebApp"),
            columns={"initial": "1", "md": "2"},
            spacing="4",
        ),
        width="100%",
        padding_y="3rem",
    )

# --- Skills Section ---
def skill_category(title, skills, icon):
    return rx.box(
        rx.vstack(
            rx.hstack(rx.icon(icon, size=24, color=COLORS["accent"]), rx.heading(title, font_size="1.2rem", font_weight="600"), spacing="3"),
            rx.flex(*[rx.badge(skill, variant="soft", color_scheme="blue", padding="0.4rem 1rem") for skill in skills], wrap="wrap", gap="3", spacing="3"),
            spacing="4",
        ),
        padding="1.5rem",
        background=COLORS["bg_card"],
        border=f"1px solid {COLORS['border']}",
        border_radius="12px",
        transition="all 0.3s ease",
        _hover={"border_color": COLORS["accent"], "box_shadow": f"0 4px 20px {COLORS['accent']}15"},
    )

def skills():
    return rx.vstack(
        section_heading("Technical Skills"),
        rx.grid(
            skill_category("Languages", ["Python", "Dart", "SQL", "Yaml"], "code"),
            skill_category("ML/AI Frameworks", ["PyTorch", "scikit-learn", "Jax", "transformers", "diffusers", "opencv", "spacy"], "cpu"),
            skill_category("Data & Analytics", ["pandas", "numpy", "matplotlib", "plotly"], "bar-chart-3"),
            skill_category("Cloud & DevOps", ["Docker", "Kubernetes", "Azure ML", "Databricks"], "cloud"),
            skill_category("Databases", ["SurrealDB", "RedisDB", "OracleDB", "MongoDB"], "database"),
            skill_category("Development Tools", ["FlutterFlow", "Git", "PowerBI", "FFmpeg"], "wrench"),
            columns={"initial": "1", "sm": "2", "lg": "3"},
            spacing="4",
        ),
        width="100%",
        padding_y="3rem",
    )

# --- Education ---
def education():
    return rx.vstack(
        section_heading("Education"),
        rx.box(
            rx.hstack(
                rx.icon("graduation-cap", size=40, color=COLORS["accent"]),
                rx.vstack(
                    rx.heading("Bachelor of Engineering in Information Technology", font_size="1.3rem", font_weight="600"),
                    rx.text("Muffakham Jah College of Engineering and Technology", font_size="1.1rem", color=COLORS["text_secondary"]),
                    rx.text("July 2018 - June 2022 • Hyderabad, India", font_size="0.95rem", color=COLORS["text_secondary"]),
                ),
                spacing="4",
            ),
            padding="2rem",
            background=COLORS["bg_card"],
            border=f"1px solid {COLORS['border']}",
            border_radius="12px",
        ),
        width="100%",
        padding_y="3rem",
    )

# --- Contact ---
def contact():
    return rx.vstack(
        section_heading("Get In Touch"),
        rx.box(
            rx.vstack(
                rx.text("I'm always open to new opportunities and exciting projects.", font_size="1.1rem", color=COLORS["text_secondary"], text_align="center"),
                rx.hstack(
                    rx.link(rx.button("Email Me", size="3", variant="solid", color_scheme="violet"), href="mailto:rohanoxob3000@gmail.com"),
                    rx.link(rx.button("LinkedIn", size="3", variant="outline", color_scheme="violet"), href="https://www.linkedin.com/in/rohan-cherukuri-5877b2182", is_external=True),
                    spacing="4",
                ),
                spacing="4",
                align="center",
            ),
            padding="3rem",
            background=f"linear-gradient(135deg, {COLORS['accent']}10 0%, {COLORS['gradient_end']}10 100%)",
            border=f"1px solid {COLORS['border']}",
            border_radius="12px",
        ),
        width="100%",
        padding_y="3rem",
    )

# --- Footer ---
def footer():
    return rx.vstack(
        rx.divider(border_color=COLORS["border"], margin_y="2rem"),
        rx.text(f"© {datetime.date.today().year} Rohan Cherukuri • Built with Reflex", color=COLORS["text_secondary"], font_size="0.9rem"),
        rx.hstack(
            rx.link(rx.icon("github", size=20, color=COLORS["text_secondary"]), href="https://github.com/Rohancherukuri", is_external=True),
            rx.link(rx.icon("linkedin", size=20, color=COLORS["text_secondary"]), href="https://www.linkedin.com/in/rohan-cherukuri-5877b2182", is_external=True),
            rx.link(rx.icon("mail", size=20, color=COLORS["text_secondary"]), href="mailto:rohanoxob3000@gmail.com"),
            spacing="4",
            justify="center",
        ),
        align="center",
        width="100%",
        padding_bottom="3rem",
    )

# --- Scroll to Top ---
def scroll_to_top():
    return rx.box(
        rx.button(
            rx.icon("arrow-up", size=20),
            position="fixed",
            bottom="2rem",
            right="2rem",
            size="3",
            variant="solid",
            color_scheme="violet",
            border_radius="full",
            box_shadow="0 4px 20px rgba(0,0,0,0.3)",
            cursor="pointer",
            z_index="999",
            on_click=rx.call_script("window.scrollTo({ top: 0, behavior: 'smooth' });"),
        ),
    )

# --- Main Page ---
def index():
    return rx.box(
        rx.container(
            rx.vstack(
                header(),
                about_me(),
                experience(),
                projects(),
                skills(),
                education(),
                contact(),
                footer(),
                spacing="0",
            ),
            max_width="1200px",
            padding_x={"initial": "1rem", "sm": "2rem", "lg": "4rem"},
        ),
        scroll_to_top(),
        bg=COLORS["bg_primary"],
        min_height="100vh",
        width="100%",
    )

# --- App Setup ---
app = rx.App(
    style={
        "font_family": "'Inter', sans-serif",
        "color": COLORS["text_primary"],
        "background": COLORS["bg_primary"],
        "scroll_behavior": "smooth",
        "@keyframes gradientShift": ANIMATIONS["gradientShift"],
        "@keyframes fadeInUp": ANIMATIONS["fadeInUp"],
    },
    stylesheets=["https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"]
)

app.add_page(
    index,
    title="Rohan Cherukuri - Machine Learning Engineer",
    description="Portfolio of Rohan Cherukuri, a Machine Learning Engineer specializing in AI, Computer Vision, and NLP",
    meta=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)
