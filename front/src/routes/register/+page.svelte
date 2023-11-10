<script lang="ts">
    import { url } from "$lib";
    import Auth from "$lib/Auth.svelte";

    let on_register = async (e: CustomEvent<{ login: string; password: string }>) => {
        let response = fetch(url("registration"), {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                login: e.detail.login,
                password: e.detail.password,
                first_name: "TODO", // TODO
                last_name: "TODO" // TODO
            })
        });
        let s = await response;
        console.log(s);
    };
</script>

<Auth kind="register" on:confirm={on_register} />
