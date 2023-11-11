<script lang="ts">
    import { goto } from "$app/navigation";
    import { page } from "$app/stores";
    import Hr from "$lib/Hr.svelte";
    import Icon from "$lib/Icon.svelte";
    import { journal, journal_by_id, type JournalEntry } from "$lib/core/journal";
    import { onMount } from "svelte";
    import Images from "./images.svelte";
    import { secure_fetch } from "$lib/core/auth";

    let id = $page.params.id;
    let entry: JournalEntry;

    let text: string;
    let base64: string | undefined = undefined;

    onMount(async () => {
        entry = await journal_by_id(Number(id));
        text = entry.text ? entry.text : "";
    });

    function readFile(input: HTMLInputElement) {
        let file = input.files![0];

        let reader = new FileReader();

        reader.readAsDataURL(file);

        reader.onload = function () {
            let base64 = reader.result;
            if (typeof base64 == "string") {
                base64 = base64.replace("data:image/png;base64,", "");
                
            }
        };

        reader.onerror = function () {
            console.error(reader.error);
        };
    }

    async function on_click() {
        goto("/journal");
        let a = secure_fetch(`journal/note/${id}`, {
            method: "POST",
            body: JSON.stringify(base64 ? { text, photo: base64 } : { text }),
            headers: {
                "Content-Type": "application/json"
            },            
        });
        console.log(await a);
    }
</script>

<article>
    <header>
        <button on:click={() => goto("/journal")}>
            <Icon kind="back" />
        </button>
        <h1>Дневник</h1>
    </header>
    <Hr />
    <!-- TODO: Надпись "максимум 300 символов" -->
    <textarea placeholder="Скажите, что вы думаете об этом месте" />
    <Images />
    <label class="upload-image">
        <Icon kind="plus" />
        Добавить фото
        <input
            id="picField"
            type="file"
            style="display: none"
            name="image"
            accept="image/gif,image/jpeg,image/jpg,image/png"
            multiple
            on:change={(t) => readFile(t.currentTarget)}
        />
    </label>
    <button on:click={on_click}>Сохранить изменения</button>
</article>

<style lang="scss">
    article {
        display: flex;
        flex-direction: column;
        height: 100dvh;
        background-color: var(--white1);
        border-radius: 8px;
        padding: 0 16px;
        --margin: 0 -20px;

        header {
            display: flex;
            flex: 0 0 48px;
            align-items: center;
            button {
                --icon-size: 16px;
                padding: {
                    top: 16px;
                    bottom: 10px;
                    right: 12px;
                }
                border: 0;
                background-color: transparent;
                cursor: pointer;
            }
            h1 {
                font-size: 18px;
                height: 24px;
                line-height: 24px;
                font-weight: bold;
            }
        }
        textarea {
            flex: 1;
            resize: none;
            margin: 16px 0;
            height: 90px;
            border: 0;
            color: var(--black);
            font-size: 15px;
            outline: none;
            &::placeholder {
                color: var(--gray-text);
            }
        }
        .upload-image {
            display: flex;
            gap: 8px;
            font-size: 15px;
            --icon-size: 12px;
            input[type="file"] {
                display: none;
            }
        }
        > button {
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: var(--emphis2);
            height: 40px;
            border: 0;
            border-radius: 8px;
            color: var(--white1);
            font-size: 15px;
            margin: {
                top: 24px;
                bottom: 12px;
            }
        }
    }
</style>
