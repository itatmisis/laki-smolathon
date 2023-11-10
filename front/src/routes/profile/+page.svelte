<script>
    import Hr from "$lib/Hr.svelte";
    import Statistics from "../journal/Statistics.svelte";
    import Achievement from "./Achievements.svelte";
    import GotoButton from "./GotoButton.svelte";
    import ProfileInfo from "./ProfileInfo.svelte";
    import SimpleButton from "./SimpleButton.svelte";
</script>

<section>
    <ProfileInfo name="Ivan Pirogov" />
    <Statistics />
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

<style lang="scss">
    section {
        flex: 1;
        padding: 16px;
        display: flex;
        flex-direction: column;
        align-items: stretch;
        gap: 8px;
        max-height: calc(100vh - 60px - 2 * 20px);
        overflow-y: scroll;
        menu {
            display: flex;
            flex-direction: column;
            align-items: start;
        }
    }
</style>
