<script lang="ts">
    import { goto } from "$app/navigation";
    import CategoryChip from "$lib/CategoryChip.svelte";
    import Icon from "$lib/Icon.svelte";
    import PlaceHeader from "$lib/PlaceHeader.svelte";
    import { CategoriesIcons, type Category, type Place } from "$lib/core/places";

    export let place: Place;
    $: _category = CategoriesIcons[place.category];

    let percent = 100;
    $: _percent = `${percent}%`;
</script>

<article>
    <header>
        <CategoryChip title={place.category} color={_category.color} icon={_category.icon} small />
        <button class="map"><Icon kind="map" /></button>
    </header>

    <PlaceHeader title={place.name} address1={place.address.line1} address2={place.address.line2} />
    <!-- TODO: Градиент по мере заполнения дневника -->
    <button
        class="edit"
        style:--progress={_percent}
        on:click={() => goto(`/journal/edit/${place.id}`)}
    >
        <span>Продолжить заполнение</span>
        <!-- TODO: <span>{percent.toFixed(0)}%</span> -->
    </button>
</article>

<style lang="scss">
    article {
        display: flex;
        flex-direction: column;
        align-items: stretch;

        background-color: var(--white1);
        padding: 16px;
        border-radius: 8px;
        header {
            display: flex;
            align-items: start;
            justify-content: space-between;
            height: 40px;
        }
    }
    button {
        border: 0;
        border-radius: 8px;
        &.map {
            height: 40px;
            width: 40px;
            --icon-size: 20px;
            background-color: var(--system-gray-base);
        }
        &.edit {
            display: flex;
            align-items: center;
            justify-content: space-between;

            padding: 0 20px;
            margin-top: 15px;

            color: white;
            background-color: var(--emphis2);
            font-size: 15px;
            text-align: center;
            background: linear-gradient(
                to right,
                var(--emphis2) 0%,
                var(--emphis2) var(--progress),
                var(--emphis2-dark) var(--progress),
                var(--emphis2-dark) 100%
            );

            height: 40px;
            align-self: stretch;
        }
    }
</style>
