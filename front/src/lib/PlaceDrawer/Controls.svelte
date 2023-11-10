<script lang="ts">
    export let main_button: "route" | "review";
</script>

<div class="controls">
    <div class="row">
        <button class="check">Отметиться</button>
        <button class="journal">Перейти к дневнику</button>
    </div>
    <div class="row">
        <button class="main">
            {#if main_button == "route"}
                Построить маршрут
                <br />
                <span class="small">Яндекс.Карты &dash;&dash;&gt;</span>
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
        color: var(--black);
        background-color: var(--white1);
        border: 1px solid var(--gray-system);
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
            color: var(--white1);
            background-color: var(--emphis2);
            font-size: 15px;
            margin-bottom: 16px;
            .small {
                font-size: 13px;
            }
        }
    }
</style>
