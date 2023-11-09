<script lang="ts">
    import CategoryChip from "$lib/CategoryChip.svelte";
    import Icon from "$lib/Icon.svelte";
    import PlaceHeader from "$lib/PlaceHeader.svelte";

    export let title: string;
    export let address1: string;
    export let address2: string;
</script>

<article>
    <button class="map"><Icon kind="map" /></button>

    <CategoryChip category="Собор"/>
    <PlaceHeader {title} {address1} {address2} />
    <!-- TODO: Градиент по мере заполнения дневника -->
    <button class="edit">
        <span>Продолжить заполнение</span>
        <!-- svelte-ignore a11y-missing-attribute -->
        <img src={`icons/arrow-right-long.svg`} />
    </button>
</article>

<style lang="scss">
    article {
        position: relative;
        display: flex;
        flex-direction: column;
        background-color: #d9d9d9;
        padding: 16px;
        align-items: start;
        border-radius: 8px;
    }
    button {
        border: 0;
        border-radius: 8px;
        background-color: #727272;
        &.map {
            position: absolute;
            right: 15px;
            top: 15px;

            height: 40px;
            width: 40px;
            --icon-invert: 1;
            --icon-size: 20px;
        }
        &.edit {
            display: flex;
            align-items: center;
            justify-content: space-between;

            padding: 0 20px;
            margin-top: 15px;

            color: white;
            font-size: 15px;

            height: 40px;
            align-self: stretch;

            > img {
                transform: translateY(4px);
            }
        }
    }
</style>
