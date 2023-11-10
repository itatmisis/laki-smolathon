<script lang="ts">
    export let main_button: "route" | "review";
    $: main_button_color = main_button == "route" ? "#ff0000" : "#fe9a28";
</script>

<div class="controls">
    <div class="row">
        <button class="check">Отметиться</button>
        <button class="journal">Перейти к дневнику</button>
    </div>
    <div class="row">
        <button class="main" style:background-color={main_button_color}>
            {#if main_button == "route"}
                Построить маршрут
                <br />
                <span class="secondary-text">Яндекс.Карты &dash;&dash;&gt;</span>
            {:else if main_button == "review"}
                Написать отзыв
            {/if}
        </button>
    </div>
</div>

<style lang="scss">
    .controls {
        display: flex;
        flex-direction: column;
        gap: 8px;
        > .row {
            display: flex;
            justify-content: stretch;
            gap: 8px;
        }
    }
    button {
        color: white;
        background-color: #727272;
        border: 0;
        border-radius: 8px;
        flex: 1;
        padding: 10px;
        &.journal {
            flex: 2;
        }
        &.main {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
    }
</style>
