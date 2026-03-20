from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultPhoto,
)
from py_yt import VideosSearch
from ShrutiMusic import app
from ShrutiMusic.utils.inlinequery import answer
from config import BANNED_USERS


@app.on_inline_query(~BANNED_USERS)
async def inline_query_handler(client, query):
    text = query.query.strip()
    results_list = []

    # 🔹 Empty query → default panel
    if not text:
        try:
            return await client.answer_inline_query(
                query.id,
                results=answer,
                cache_time=5,
                is_personal=True
            )
        except:
            return

    try:
        search = VideosSearch(text, limit=15)
        results = (await search.next()).get("result", [])

        for vid in results:
            title = vid["title"]
            duration = vid.get("duration", "Live")
            views = vid["viewCount"]["short"]
            thumbnail = vid["thumbnails"][0]["url"].split("?")[0]
            channel = vid["channel"]["name"]
            channellink = vid["channel"]["link"]
            link = vid["link"]
            published = vid["publishedTime"]

            description = f"{views} • {duration} • {channel}"

            buttons = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("▶️ Watch", url=link),
                    ],
                ]
            )

            caption = f"""
🎧 <b>{title}</b>

⏱ Duration: {duration}
👀 Views: <code>{views}</code>
📺 Channel: <a href="{channellink}">{channel}</a>
📅 Published: {published}

✨ Powered by {app.mention}
"""

            results_list.append(
                InlineQueryResultPhoto(
                    photo_url=thumbnail,
                    thumb_url=thumbnail,
                    title=title,
                    description=description,
                    caption=caption,
                    reply_markup=buttons,
                )
            )

        return await client.answer_inline_query(
            query.id,
            results=results_list,
            cache_time=5,
            is_personal=True
        )

    except Exception as e:
        print(e)
        return
