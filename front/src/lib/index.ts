export type IconKind =
    | "heart"
    | "marker"
    | "arrow-right"
    | "map"
    | "profile"
    | "journal"
    | "pencil"
    | "pointer"
    | "monument"
    | "history"
    | "church"
    | "museum";

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
