<script lang="ts">
    export let value: string;
    export let placeholder: string;
</script>

<input
    type="search"
    {placeholder}
    autocomplete="off"
    spellcheck="false"
    bind:value
    on:input
    on:change
    on:focus
    on:blur
    on:keydown
/>

<style lang="scss">
    input[type="search"]:focus {
        box-shadow: 0 0 3px 0 #1183d6;
        border-color: #1183d6;
        outline: none;
    }

    input {
        border: 1px solid #555;
        width: 100%;
        padding: 9px 4px 9px calc(20px + 24px + 5px);
        background: var(--white1)
            url("icons/search.svg")
            no-repeat 18px center;
        background-size: 18px;
        border: 0;
        border-radius: 8px;
        &::placeholder {
            font-size: 15px;
            font-family: "Roboto Slab", sans-serif;
        }
    }
</style>
