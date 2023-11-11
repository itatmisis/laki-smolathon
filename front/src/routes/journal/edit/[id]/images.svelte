<script lang="ts">
    import Icon from "$lib/Icon.svelte";

    let images = [
        "https://avatars.dzeninfra.ru/get-zen_doc/3472554/pub_5f212b3a3bfc8f1d386943c4_5f212c42a1687b686cd114d5/scale_1200"
    ];
    let on_click = (src: string) => {
        const index = images.indexOf(src);
        if (index > -1) {
            images.splice(index, 1);
            images = images;
        }
    };
    export function add_image() {
        alert("Added");
    }
</script>

<section>
    {#each images as src}
        <article>
            <button on:click={() => on_click(src)}><Icon kind="cancel" /></button>
            <!-- svelte-ignore a11y-missing-attribute -->
            <img {src} />
        </article>
    {/each}
</section>

<style lang="scss">
    section {
        margin-bottom: 20px;
        article {
            position: relative;
            width: 80px;
            height: 80px;
            button {
                display: flex;
                align-items: center;
                justify-content: center;
                border: 0;
                border-radius: 8px;
                position: absolute;
                width: 16px;
                height: 16px;
                right: 4px;
                top: 4px;
                --icon-size: 8px;
            }
            img {
                width: 80px;
                height: 80px;
                border-radius: 8px;
            }
        }
    }
</style>
