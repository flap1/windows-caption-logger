import uiautomation as auto
import time
import difflib

OUTPUT_FILE = "captions_log.txt"

def main():
    window = auto.WindowControl(searchDepth=1, Name="ライブ キャプション")
    if not window.Exists(3, 1):
        print("ライブキャプションのウィンドウが見つかりません。起動してから実行してください。")
        return

    print("ライブキャプションを監視開始...")

    last_line = ""

    while True:
        text_elem = window.TextControl()
        full_text = text_elem.Name.strip() if text_elem else ""
        lines = [line.strip() for line in full_text.splitlines() if line.strip()]

        if not lines:
            time.sleep(0.5)
            continue

        current_last = lines[-1]  # 進行中の最後の行

        if current_last != last_line:
            # 差分（新しく追加された部分だけ取り出す）
            diff = difflib.SequenceMatcher(None, last_line, current_last)
            _, _, _, j1, j2 = diff.get_opcodes()[-1]
            new_part = current_last[j1:j2]

            if new_part.strip():
                with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
                    f.write(new_part + "")
                print(new_part, end=" ")

            last_line = current_last

        time.sleep(0.5)

if __name__ == "__main__":
    main()
