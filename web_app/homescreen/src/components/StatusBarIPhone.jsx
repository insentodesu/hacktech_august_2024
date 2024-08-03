import PropTypes from "prop-types";
import styles from "./StatusBarIPhone.module.css";

const StatusBarIPhone = ({ className = "" }) => {
  return (
    <div className={[styles.backgroundtrue, className].join(" ")}>
      <div className={styles.time}>
        <div className={styles.time1}>9:41</div>
      </div>
      <div className={styles.levels}>
        <div className={styles.battery}>
          <div className={styles.border} />
          <img className={styles.capIcon} alt="" src="/cap.svg" />
          <div className={styles.capacity} />
        </div>
        <img className={styles.wifiIcon} alt="" src="/wifi1.svg" />
        <img
          className={styles.cellularConnectionIcon}
          alt=""
          src="/cellular-connection.svg"
        />
      </div>
    </div>
  );
};

StatusBarIPhone.propTypes = {
  className: PropTypes.string,
};

export default StatusBarIPhone;
