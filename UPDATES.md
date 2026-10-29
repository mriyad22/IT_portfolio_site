# UI and code updates

## Design
- Refined project listing cards with improved image treatment, featured labels, category chips, hover states, clearer hierarchy, technology previews, and a more useful empty state.
- Redesigned project case-study details with a dedicated hero, breadcrumbs, image showcase, project metadata sidebar, technology chips, contact CTA, and related-project cards.
- Redesigned service details with a service hero, icon panel, benefits section, related services, and consultation CTA.
- Redesigned blog article details with author/date metadata, readable article column, cover treatment, sidebar CTA, and contact prompt.
- Added responsive layouts for mobile/tablet and reduced-motion support.
- Removed a duplicate Bootstrap Icons stylesheet include.

## Code fixes
- Registered `ProjectCatgoryModel` in Django admin so categories can be created/managed from the dashboard.
- Added `ProjectModel.technology_list` to turn the comma-separated technologies field into clean labels for the detail page.
- Optimized project queries with `select_related("category")` and made related-project handling safe when a project has no category.
- Corrected blog cover image upload path from `media/blog/` to `blog/` (Django already prefixes uploads with `MEDIA_ROOT`/`MEDIA_URL`) and added migration `blog/0004_alter_postmodel_cover_image.py`.

## Validation
- Python source files passed `compileall` syntax compilation.
- Django runtime checks and template rendering could not be executed in this workspace because Django is not installed in the active Python environment.
