<script lang="ts">
    import Icon from "$lib/Icon.svelte";
    import { filter_list } from "$lib/core/filters";
</script>

<menu>
    {#each filter_list as filter}
        <button style:background-color={filter.color}>
            <Icon kind={filter.icon} />
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
        overflow-x: scroll;
        button {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 4px;

            padding: 12px 8px;
            --icon-size: 20px;

            border-radius: 8px;
            border: 0;

            span {
                color: white;
                font-size: 13px;
            }
        }
    }
</style>
