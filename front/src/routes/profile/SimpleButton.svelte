<script lang="ts">
    export let text: string;
</script>

<button on:click>{text}</button>

<style lang="scss">
    button {
        font-size: 15px;
        text-decoration: underline;
        background-color: transparent;
        border: 0;
    }
</style>
