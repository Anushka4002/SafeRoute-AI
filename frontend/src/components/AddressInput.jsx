import { useState, useRef } from "react";
import { geocodeSearch } from "../services/api";

function AddressInput({ label, onSelect }) {
  const [query, setQuery] = useState("");
  const [suggestions, setSuggestions] = useState([]);
  const debounceRef = useRef(null);

  const handleChange = (e) => {
    const text = e.target.value;
    setQuery(text);

    if (debounceRef.current) clearTimeout(debounceRef.current);

    if (text.length < 3) {
      setSuggestions([]);
      return;
    }

    debounceRef.current = setTimeout(async () => {
      try {
        const results = await geocodeSearch(text);
        setSuggestions(results);
      } catch {
        setSuggestions([]);
      }
    }, 500);
  };

  const handleSelect = (item) => {
    setQuery(item.display_name);
    setSuggestions([]);
    onSelect(item.display_name);
  };

  return (
    <div className="address-input">
      <label>{label}</label>
      <input
        type="text"
        value={query}
        onChange={handleChange}
        placeholder={`Enter ${label.toLowerCase()}`}
      />
      {suggestions.length > 0 && (
        <ul className="suggestions">
          {suggestions.map((item, idx) => (
            <li key={idx} onClick={() => handleSelect(item)}>
              {item.display_name}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default AddressInput;