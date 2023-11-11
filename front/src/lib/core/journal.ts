import { secure_fetch } from "./auth";

export type JournalEntry = {
    id: number,
    id_user: number,
    id_location: number,
    text?: string,
    photo?: string
};

export async function check(id: number) {
    let response = await secure_fetch(`map/location/${id}`, {
        method: "POST",
    });
    console.log(response);
}

export async function journal(): Promise<JournalEntry[]> {
    let response = await secure_fetch("journal/note");
    let json: Array<any> = await response.json();
    let list: Array<JournalEntry> = [];
    for (const entry of json) {
        list.push(entry);
    }
    return list;
}

export async function journal_by_location(id: number): Promise<JournalEntry[]> {
    let response = await secure_fetch(`journal/note/location/${id}`);
    let json: Array<any> = await response.json();
    let list: Array<JournalEntry> = [];
    for (const entry of json) {
        list.push(entry);
    }
    console.log(list);
    return list;
}

export async function journal_by_id(id: number): Promise<JournalEntry> {
    let response = await secure_fetch(`journal/note/${id}`);
    return await response.json();
}
