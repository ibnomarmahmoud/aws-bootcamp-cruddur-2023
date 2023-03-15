from datetime import datetime, timedelta, timezone
from lib.db import pool, query_wrap_array
from opentelemetry import trace
tracer = trace.get_tracer("new_trace")

import watchtower
import logging
from time import strftime

class HomeActivities:
  def run(LOGGER):
    LOGGER.info('Hello Cloudwatch! from  /api/activities/home')
    with tracer.start_as_current_span("Home-Activities-span"):
      span = trace.get_current_span()
      span.set_attribute("app.endpoint", "Home_Activities")
      now = datetime.now(timezone.utc).astimezone()
      sql = query_wrap_array("""
      SELECT
        activities.uuid,
        users.display_name,
        users.handle,
        activities.message,
        activities.replies_count,
        activities.reposts_count,
        activities.likes_count,
        activities.reply_to_activity_uuid,
        activities.expires_at,
        activities.created_at
      FROM public.activities
      LEFT JOIN public.users ON users.uuid = activities.user_uuid
      ORDER BY activities.created_at DESC
      """)
      print(sql)
      with tracer.start_as_current_span("Home-Activities-span-Inner") as inner_span:
        with pool.connection() as conn:
          with conn.cursor() as cur:
            cur.execute(sql)
            json = cur.fetchone()
        return json[0]


