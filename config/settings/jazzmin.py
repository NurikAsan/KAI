JAZZMIN_SETTINGS = {
    "site_title": "Администрирование библиотеки",
    "site_header": "Кыргызский Авиационный Институт",
    "site_brand": "КАИ",
    "site_logo_classes": "img-circle",
    "welcome_sign": "Добро пожаловать в Кыргызский Авиационный Институт",
    "copyright": "Acme Library Ltd",

    "show_sidebar": True,
    "navigation_expanded": True,

    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},

        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},

        {"model": "auth.User"},
    ],

    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],

    "order_with_respect_to": [
        'moderator',
        "auth",
        #add ordering
    ],

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        #add icons for each model
    },

    "hide_models": [],

    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    "language_chooser": False,
}

JAZZMIN_UI_TWEAKS = {
    "theme": "default",  # Theme to use
    "dark_mode_theme": None,  # Optional dark mode theme
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,  # Remove the navbar border
    "navbar_fixed": False,  # Navbar fixed at the top
    "layout_fixed": False,  # Fixed layout
    "footer_fixed": False,  # Fixed footer
    "sidebar": "sidebar-dark-primary",  # Sidebar theme
    "sidebar_nav_small_text": False,  # Smaller text in sidebar
    "sidebar_disable_expand": False,  # Disable sidebar expand
    "sidebar_nav_child_indent": True,  # Indent child menu items
    "sidebar_nav_compact_style": False,  # Compact style for sidebar
    "sidebar_nav_legacy_style": False,  # Legacy style for sidebar
    "sidebar_nav_flat_style": False,  # Flat style for sidebar
    "brand_small_text": False,  # Small text for brand
    "brand_color": None,  # Brand color
    "accent": "accent-primary",  # Accent color
    "sidebar_fixed": True,  # Fixed sidebar
    "topmenu_links": [],  # Top menu links
    "usermenu_links": [],  # User menu links
    "usermenu_search": False,  # User menu search
    "breadcrumbs": True,  # Show breadcrumbs
    "show_sidebar_scrollbars": True,  # Show sidebar scrollbars
    "navbar_small_text": False,  # Small text for navbar
    "navbar_search": False,  # Show navbar search
    "navbar_language_selector": False,  # Show navbar language selector
    "navbar_right_icons": False,  # Show right icons in navbar
    "navbar_right": [],  # Right icons in navbar
    "navbar_notifications": [],  # Navbar notifications
    "navbar_links": [],  # Navbar links
    "navbar_user": True,  # Show user menu in navbar
    "navbar_user_avatar": False,  # Show user avatar in navbar
    "sidebar_search": False,  # Show sidebar search
    "sidebar_user": True,  # Show user in sidebar
    "sidebar_user_avatar": False,  # Show user avatar in sidebar
    "sidebar_collapse": False,  # Collapse sidebar
    "sidebar_mini": True,  # Mini sidebar
    "sidebar_mini_hover_expand": False,  # Hover expand mini sidebar
    "footer_text": None,  # Footer text
    "footer_links": [],  # Footer links
}