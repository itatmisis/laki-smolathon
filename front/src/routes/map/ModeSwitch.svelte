<script lang="ts">
    export let selected: "one" | "two" = "one";

    function swap() {
        if (selected == "one") {
            selected = "two";
        } else {
            selected = "one";
        }
    }
</script>

<menu>
    <button class:selected={selected=="one"} on:click={swap}>Режим один</button>
    <button class:selected={selected=="two"} on:click={swap}>Режим два (название)</button>
</menu>

<style lang="scss">
    menu {
        display: flex;
        position: absolute;
        justify-content: stretch;
        height: 32px;

        top: var(--gap);
        left: var(--gap);
        right: var(--gap);
        gap: var(--gap);

        & :nth-child(1) {
            flex: 1 0 100px;
        }
        & :nth-child(2) {
            flex: 2 0 100px;
        }
        button {
            border-radius: 8px;
            border: 0;
            background-color: var(--button-color, var(--background-color, white));
            &.selected {
                color: white;
                background-color: var(--selected-color, #727272);
            }
            &:not(.selected) {
                border: 1px #D9D9D9 solid;
            }
        }
    }
</style>