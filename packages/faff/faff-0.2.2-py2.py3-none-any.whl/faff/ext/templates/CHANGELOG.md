# Change Log
{% for audience in audiences %}
## {{ audience.name }}
{% for tag in audience.tags %}
### [{{ tag.name }}]{% if tag.date %} - {{ tag.date }}{% endif %}
{% for category in tag.categories %}
#### {{ category.name }}
{% for commit in category.commits %}
-   {{ commit.subject }}
{%- endfor %}
{% endfor %}
{%- endfor %}
{%- endfor %}
