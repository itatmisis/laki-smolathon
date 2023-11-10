export type Test = {
    text: string;
    image: string;
    options: string[];
    correct_option: number;
}

export function check_test(test: Test, chosen_option: number): boolean {
    return test.correct_option == chosen_option;
}
