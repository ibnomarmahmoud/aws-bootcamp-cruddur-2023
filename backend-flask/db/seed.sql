-- this file was manually created
INSERT INTO public.users (display_name,email, handle, cognito_user_id)
VALUES
  ('Mahmoud Omar', 'abuyoussof2013@gmail.com','MahmoudOmar' ,'MOCK'),
  ('Ibarhim Omar', 'mahmoud.omar@ericsson.com','ibnomar6' ,'MOCK'),
  ('Ibrahim Mahmoud','test@gamil.com', 'Hema' ,'MOCK');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'MahmoudOmar' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  )