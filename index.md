---
layout: index
---

This is the course website for {{site.data.class.course.name}}, instructed by
{% for instructor in site.data.class.instructors -%}
{{instructor.name}} ({{instructor.email}}){% unless forloop.last %}, {% endunless -%}
{%- endfor -%}.

Below, you can explore the course by **[conceptual topics](topics)** or find the weekly schedule below, as well as the [syllabus](syllabus) that
includes contact information and a course outline.
