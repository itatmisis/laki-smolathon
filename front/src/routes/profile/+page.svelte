<script lang="ts">
    import Hr from "$lib/Hr.svelte";
    import Wrapper from "$lib/Wrapper.svelte";
    import { profile, type User } from "$lib/core/user";
    import { onMount } from "svelte";
    import Statistics from "../journal/Statistics.svelte";
    import Achievement from "./Achievements.svelte";
    import GotoButton from "./GotoButton.svelte";
    import ProfileInfo from "./ProfileInfo.svelte";
    import SimpleButton from "./SimpleButton.svelte";
    import { journal } from "$lib/core/journal";

    let user: User;
    let name: string;

    onMount(async () => {
        user = await profile();
        name = user.first_name + " " + user.last_name;
    })

    let _journal = journal();
</script>

<Wrapper>
    <section>
        <ProfileInfo {name} />
        {#await _journal then _journal}
            <Statistics journal={_journal}/>
        {/await}
        <Hr />
        <GotoButton text="Мои достижения" />
        <Hr />
        <Achievement />
        <Hr />
        <GotoButton text="Мои реакции" />
        <Hr />
        <menu>
            <SimpleButton text="Управление паролем" />
            <SimpleButton text="Сменить язык" />
            <SimpleButton text="Выйти" />
            <SimpleButton text="Удалить аккаунт" />
        </menu>
    </section>
</Wrapper>

<style lang="scss">
    section {
        flex: 1;
        padding: 16px;
        display: flex;
        flex-direction: column;
        align-items: stretch;
        gap: 8px;
        overflow-y: scroll;
        menu {
            display: flex;
            flex-direction: column;
            align-items: start;
        }
    }
</style>
