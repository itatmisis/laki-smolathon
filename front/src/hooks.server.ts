import { redirect } from '@sveltejs/kit';

export const handle = async ({ event, resolve }) => {
    const token = event.cookies.get('token');
    if (!token && !event.url.pathname.endsWith("login")) {
        throw redirect(303, '/login');
    }
    return resolve(event);
}