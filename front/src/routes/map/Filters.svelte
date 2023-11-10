<script lang="ts">
    import CategoryChip from "$lib/CategoryChip.svelte";
    import { CategoriesIcons } from "$lib/core/places";
</script>

<menu>
    {#each Object.entries(CategoriesIcons) as [title, { color, icon }]}
        <CategoryChip {title} {color} {icon}/>
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
    }
</style>
