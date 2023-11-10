import { url } from "$lib";
import { get, writable, type Readable, type Writable } from "svelte/store";

const name = "token";

function token(): string | undefined {
    var match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
    if (match) return match[2];
}

export function set_token(new_token: string) {
    document.cookie = `token=${new_token}}`;
}

export function remove_token() {
    document.cookie = "token=;expires=Thu, 01 Jan 1970 00:00:01 GMT";
}

export async function secure_fetch(path: string, init?: RequestInit) {
    let token_ = token();
    if (!token_) return Promise.reject();

    if (!init) init = {};
    init.headers = {
        Authorization: `Bearer ${token_}`,
        ...init.headers
    };
    return await fetch(url(path), init);
}
