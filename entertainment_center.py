import fresh_tomatoes
import media


toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that some to life",
                        "http://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A Marine on an Alien planet",
                     "http://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)

star_wars = media.Movie("Star Wars Episode III",
                     "An epic space drama",
                     "http://upload.wikimedia.org/wikipedia/en/thumb/9/93/Star_Wars_Episode_III_Revenge_of_the_Sith_poster.jpg/220px-Star_Wars_Episode_III_Revenge_of_the_Sith_poster.jpg",
                     "https://www.youtube.com/watch?v=5UnjrG_N8hU")
#print(star_wars.storyline)
#star_wars.show_trailer()
top_gun = media.Movie("Top Gun",
                     "Only the best make it to Top Gun",
                     "http://upload.wikimedia.org/wikipedia/en/thumb/4/46/Top_Gun_Movie.jpg/220px-Top_Gun_Movie.jpg",
                     "https://www.youtube.com/watch?v=qAfbp3YX9F0")

ghostbusters = media.Movie("Ghostbusters",
                     "I ain't afraid of no ghost!",
                     "http://upload.wikimedia.org/wikipedia/en/thumb/c/c7/Ghostbusters_cover.png/220px-Ghostbusters_cover.png",
                     "https://www.youtube.com/watch?v=cyRqR56aCKc")

bttf = media.Movie("Back to the Future",
                   "Ah, 1985.",
                   "http://upload.wikimedia.org/wikipedia/en/thumb/d/d2/Back_to_the_Future.jpg/220px-Back_to_the_Future.jpg",
                   "https://www.youtube.com/watch?v=qvsgGtivCgs")

movies = [toy_story, avatar, star_wars, top_gun, ghostbusters, bttf]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
