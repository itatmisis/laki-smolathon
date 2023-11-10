<script lang="ts">
    import { CategoriesIcons, type Category } from "$lib/core/places";

    export let category: Category;
    export let count: number;

    $: _category = CategoriesIcons[category];
</script>

<span style:--background={_category.color}>
    <mark>{count}</mark>
    {category}
</span>

<style lang="scss">
    span {
        display: flex;
        align-items: center;
        gap: 4px;
        color: var(--white2);
        padding: 8px;
        border-radius: 8px;
        font-size: 13px;
        background-color: var(--background);
        > mark {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 16px;
            height: 16px;
            text-align: center;
            color: var(--background);
            background-color: var(--white2);
            border-radius: 2px;
        }
    }
</style>
