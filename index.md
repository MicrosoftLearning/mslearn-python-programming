---
title: Get Started with Python Programming
permalink: index.html
layout: home
---

The following exercises are designed to help you practice the skills you've learned in the [Get Started with Python Programming](TODO) learning path on Microsoft Learn. Each exercise is self-contained and can be completed independently, but they are best used in conjunction with the corresponding modules on Microsoft Learn.

## Exercises

<hr>

{% assign labs = site.pages | where_exp:"page", "page.url contains '/Instructions/Exercises'" %}
{% for activity in labs  %}

### [{{ activity.lab.title }}]({{ site.github.url }}{{ activity.url }})

{% if activity.lab.level %}**Level**: {{activity.lab.level}} \| {% endif %}{% if activity.lab.duration %}**Duration**: {{activity.lab.duration}} minutes{% endif %}

*{{activity.lab.description}}*
<hr>
{% endfor %}


> **Note**: While you can complete these exercises on their own, they're designed to complement modules on [Microsoft Learn](TODO); in which you'll find a deeper dive into some of the underlying concepts on which these exercises are based.
