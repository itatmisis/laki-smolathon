<script>
    import Icon from "$lib/Icon.svelte";
    import ProfileInfo from "../ProfileInfo.svelte";
</script>

<section>
    <ProfileInfo name="Ivan Pirogov" />
    <hr/>
    <!-- <nav>
        {#each ["Мой дневник", "Мои достижения", "Мои отзывы", "Мои подписки"] as entry}
            <button>
                <span>{entry}</span>
                <Icon kind="arrow-right" />
            </button>
            <hr />
        {/each}
    </nav> -->
    <menu>
        <button>Сменить язык</button>
        <button>Выйти</button>
        <button>Удалить аккаунт</button>
    </menu>
</section>

<style lang="scss">
    section {
        flex: 1;
        margin: 20px;
        display: flex;
        flex-direction: column;
        gap: 20px;
        max-height: calc(100vh - 60px - 2 * 20px);
        hr {
            margin: 0 -20px;
        }
    }
</style>
