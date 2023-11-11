import { secure_fetch } from "./auth";

export type User = {
    id: string,
    login: string,
    first_name: string,
    last_name: string,
    date: Date,
};

export async function profile(): Promise<User> {
    let response = await secure_fetch(`user/me`);
    let json = await response.json();
    return {
        id: json.id,
        login: json.login,
        first_name: json.first_name,
        last_name: json.last_name,
        date: new Date(json.date)
    };
}
