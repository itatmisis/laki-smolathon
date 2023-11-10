<script lang="ts">
    import Input from "$lib/Input.svelte";
    import { createEventDispatcher } from "svelte";

    export let kind: "login" | "register";
    $: header = kind == "login" ? "Вход в smoll quest" : "Регистрация в smoll quest";
    $: button = kind == "login" ? "Войти" : "Зарегистрироваться";
    $: link_text = kind == "login" ? "Создать аккаунт" : "У меня уже есть аккаунт";
    $: link_url = kind == "login" ? "register" : "login";

    let dispatch = createEventDispatcher<{ confirm: { login: string, password: string } }>();
    let login: string;
    let password: string;
</script>

<main>
    <h1>{header}</h1>
    <div class="inputs">
        <Input bind:value={login} label="Логин" />
        <Input bind:value={password} label="Пароль" type="password" />
    </div>
    <button on:click={() => dispatch("confirm", { login, password })}>{button}</button>
    <a href={link_url}>{link_text}</a>
</main>

<style lang="scss">
    main {
        height: 100dvh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: stretch;
        padding: 20px;
        h1 {
            text-align: center;
            font-size: 24px;
            font-weight: normal;
        }
        .inputs {
            display: flex;
            flex-direction: column;

            margin-top: 16px;
            margin-bottom: 20px;
            gap: 12px;
        }
        button {
            color: var(--white1);
            font-size: 15px;
            background-color: var(--emphis2);
            border: 0;
            height: 40px;
            border-radius: 8px;
        }
        a {
            color: var(--emphis2);
            text-align: center;
            margin-top: 12px;
        }
    }
</style>
