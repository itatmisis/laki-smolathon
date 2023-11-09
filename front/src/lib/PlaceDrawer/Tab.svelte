<script lang="ts">
    export let text: string;
    export let num: number | undefined = undefined;
    export let selected: boolean = false;
</script>

<button on:click class:selected>
    {text}
    {#if num}
        <mark>{num}</mark>
    {/if}
</button>

<style lang="scss">
    button {
        display: flex;
        gap: 5px;
        align-items: center;
        background-color: white;
        border: 1px solid #727272;
        border-radius: 8px;
        padding: 4px 6px;
        font-size: 13px;
        &.selected {
            color: white;
            background-color: #727272;
        }
        mark {
            display: flex;
            align-items: center;
            justify-content: center;
            color: #d9d9d9;
            background-color: #727272;
            width: 16px;
            height: 16px;
        }
    }
</style>
