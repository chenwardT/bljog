from django.db import models


class PostManager(models.Manager):
    def list_archived_months(self):
        from django.db import connection

        cursor = connection.cursor()
        cursor.execute("""
          SELECT DISTINCT to_char(p.created, 'Month') AS month_name,
                          extract(month from p.created) AS month_no,
                          CAST(extract(year from p.created) AS text) AS year
          FROM blog_post p
          ORDER BY year DESC,
                   month_no DESC""")
        months_and_years = []
        for row in cursor.fetchall():
            month = row[0].strip()
            year = row[2]
            months_and_years.append('{0} {1}'.format(month, year))
        return months_and_years