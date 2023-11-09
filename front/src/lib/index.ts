export type IconKind =
    | "heart"
    | "marker"
    | "arrow-right"
    | "map"
    | "profile"
    | "journal"
    | "pencil";

export type Place = {
    name: string;
    description: string;
    category: Category;
};

export type JournalEntry = {
    user_photo: string | undefined;
    achievements: Achievement[];
};

type Achievement = { name: string };

type Category = (typeof Categories)[number];

const Categories = ["Музеи", "Храмы", "Соборы", "Памятники"] as const;

export type Review = {
    photo: string;
    name: string;
    text: string;
    posted_at: string;
};
