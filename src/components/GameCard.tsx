import { Link } from "react-router-dom";
import type { Game } from "../types";
import { useAuth } from "../lib/auth";
import { IconHeart, IconHeartFilled, IconStar } from "./icons";
import { GENRES } from "../data/genres";
import { handleCoverError } from "../lib/imageFallback";
import "./gameCard.css";

interface GameCardProps {
  game: Game;
  index?: number;
}

export default function GameCard({ game }: GameCardProps) {
  const { user, toggleWishlist } = useAuth();
  const wished = user?.wishlist.includes(game.slug) ?? false;

  return (
    <article className="game-card">
      <Link to={`/games/${game.slug}`} className="game-card__media">
        <img
          src={game.thumbnail}
          alt={game.name}
          loading="lazy"
          onError={handleCoverError}
        />
        <button
          className="game-card__wish"
          aria-label="Toggle wishlist"
          onClick={(e) => {
            e.preventDefault();
            if (!user) return;
            toggleWishlist(game.slug);
          }}
        >
          {wished ? <IconHeartFilled /> : <IconHeart />}
        </button>
      </Link>
      <div className="game-card__body">
        <p className="label-caps">{GENRES[game.genre].name}</p>
        <Link to={`/games/${game.slug}`}>
          <h3 className="game-card__title">{game.name}</h3>
        </Link>
        <p className="game-card__tagline">{game.tagline}</p>
        <div className="game-card__meta">
          <span className="game-card__rating">
            <IconStar /> {game.rating.toFixed(1)}
          </span>
          <span>{game.developer}</span>
        </div>
      </div>
    </article>
  );
}
