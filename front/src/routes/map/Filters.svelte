<script lang="ts">
    import Icon from "$lib/Icon.svelte";
    import { filter_list } from "$lib/core/filters";
</script>

<menu>
    {#each filter_list as filter}
        <button>
            <Icon kind={filter.icon}/>
            <span>{filter.title}</span>
        </button>
    {/each}
</menu>

<style lang="scss">
    menu {
        display: flex;
        position: absolute;
        left: var(--gap);
        right: var(--gap);
        bottom: var(--gap);
        gap: var(--gap);
    }
    button {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;

        border-radius: 0;
        border: 0;
        background-color: var(--button-color, var(--background-color, white));

        span {
            font-size: 13px;
        }
    }
</style>
