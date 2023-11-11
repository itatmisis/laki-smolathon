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

export function url(partial: string): string {
    return `https://laki.itatmisis.ru/backend/${partial}`;
}
