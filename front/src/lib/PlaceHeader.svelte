<script lang="ts">
    export let title: string;
    export let address1: string;
    export let address2: string;
</script>

<article>
    <h1>{title}</h1>
    <address class="line1">{address1}</address>
    <address class="line2">{address2}</address>
</article>

<style lang="scss">
    article {
        display: flex;
        flex-direction: column;

        h1 {
            font-weight: bold;
            font-size: 15px;
            height: 24px;
        }
        address {
            font-style: normal;
            &.line1 {
                font-size: 15px;
                color: #000000;
                height: 24px;
            }
            &.line2 {
                color: #727272;
                font-size: 13px;
                height: 20px;
            }
        }
    }
</style>
