export type IconKind =
    | "heart"
    | "marker"
    | "arrow-right"
    | "map"
    | "profile"
    | "journal"
    | "pointer"
    | "monument"
    | "history"
    | "church"
    | "museum"
    | "filter"
    | "ok"
    | "cancel"
    | "edit"
    | "plus"
    | "minus"
    | "back"
    | "forward";

export type JournalEntry = {
    user_photo: string | undefined;
    achievements: Achievement[];
};

type Achievement = { name: string };

export type Review = {
    photo: string;
    name: string;
    text: string;
    posted_at: string;
};

export function url(partial: string): string {
    return `https://laki.itatmisis.ru/backend/${partial}`;
}
