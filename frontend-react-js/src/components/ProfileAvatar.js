import './ProfileAvatar.css';

export default function ProfileAvatar(props) {
  const backgroundImage = `url("https://assets.eg-cruddur.online/avatars/processed/meccano-purple-forklift2.JPG")`;
  const styles = {
    backgroundImage: backgroundImage,
    backgroundSize: 'cover',
    backgroundPosition: 'center',
  };

  return (
    <div 
      className="profile-avatar"
      style={styles}
    ></div>
  );
}