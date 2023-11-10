<script lang="ts">
    import { url } from "$lib";
    import Auth from "$lib/Auth.svelte";
    import { set_token } from "$lib/core/auth";

    let on_login = async (e: CustomEvent<{ login: string; password: string }>) => {
        let credentials = {
            username: e.detail.login,
            password: e.detail.password
        };
        let response = await fetch(url("login"), {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: new URLSearchParams(credentials)
        });
        let body = await response.json();
        let token = body.access_token;
        set_token(token);
    };
</script>

<Auth kind="login" on:confirm={on_login} />
