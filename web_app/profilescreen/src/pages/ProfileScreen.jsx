import styles from "./ProfileScreen.module.css";

const ProfileScreen = () => {
  return (
    <div className={styles.profileScreen}>
      <div className={styles.statusBarIphone}>
        <div className={styles.time}>
          <div className={styles.time1}>9:41</div>
        </div>
        <div className={styles.levels}>
          <div className={styles.battery}>
            <div className={styles.border} />
            <img className={styles.capIcon} alt="" src="/cap.svg" />
            <div className={styles.capacity} />
          </div>
          <img className={styles.wifiIcon} alt="" src="/wifi.svg" />
          <img
            className={styles.cellularConnectionIcon}
            alt=""
            src="/cellular-connection.svg"
          />
        </div>
      </div>
      <div className={styles.depth0Frame0}>
        <div className={styles.depth1Frame0}>
          <div className={styles.depth2Frame0}>
            <div className={styles.depth3Frame0}>
              <img className={styles.vector0} alt="" src="/vector--0.svg" />
              <div className={styles.depth4Frame0} />
            </div>
          </div>
          <div className={styles.depth2Frame1}>
            <b className={styles.b}>Личный кабинет</b>
          </div>
        </div>
        <div className={styles.depth1Frame1}>
          <div className={styles.depth2Frame01}>
            <img
              className={styles.depth3Frame01}
              alt=""
              src="/depth-3-frame-0@2x.png"
            />
            <div className={styles.depth3Frame02}>
              <div className={styles.depth4Frame1}>
                <div className={styles.depth5Frame0}>
                  <b className={styles.b1}>Алексей Шевцов</b>
                </div>
                <div className={styles.depth5Frame1}>
                  <div className={styles.div}>Проверенный специалист</div>
                </div>
              </div>
            </div>
            <div className={styles.depth4Frame11}>
              <div className={styles.depth5Frame01}>
                <b className={styles.b1}>3000 ₽</b>
              </div>
              <div className={styles.depth5Frame11} />
            </div>
            <div className={styles.depth5Frame12} />
          </div>
        </div>
        <div className={styles.depth1Frame7}>
          <b className={styles.b1}>Текущий проект</b>
        </div>
        <div className={styles.depth1Frame2}>
          <div className={styles.depth2Frame02}>
            <img
              className={styles.depth3Frame03}
              alt=""
              src="/depth-3-frame-01@2x.png"
            />
            <div className={styles.depth3Frame1}>
              <div className={styles.depth4Frame01}>
                <b className={styles.b}>Парк “Каштановая роща”</b>
              </div>
              <div className={styles.depth4Frame12}>
                <div className={styles.depth5Frame02}>
                  <div className={styles.div}>Завершено на 75%</div>
                </div>
                <div className={styles.depth5Frame13}>
                  <div className={styles.depth6Frame0}>
                    <b className={styles.b5}>Подробнее</b>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div className={styles.depth1Frame3}>
          <b className={styles.b1}>Расписание смен</b>
        </div>
        <div className={styles.depth1Frame4}>
          <div className={styles.depth2Frame03}>
            <div className={styles.depth3Frame0}>
              <img className={styles.vector0} alt="" src="/vector--01.svg" />
              <div className={styles.depth4Frame02} />
            </div>
          </div>
          <div className={styles.depth2Frame11}>
            <div className={styles.depth3Frame05}>
              <div className={styles.div2}>Следующая смена</div>
            </div>
            <div className={styles.depth3Frame11}>
              <div className={styles.div3}>Завтра в 8:00</div>
            </div>
          </div>
        </div>
        <div className={styles.depth1Frame5}>
          <div className={styles.depth2Frame04}>
            <div className={styles.depth3Frame06}>
              <div className={styles.depth6Frame0}>
                <b className={styles.b5}>Начать смену</b>
              </div>
            </div>
            <div className={styles.depth3Frame12}>
              <div className={styles.depth6Frame0}>
                <b className={styles.b5}>Пропустить смену</b>
              </div>
            </div>
          </div>
        </div>
        <div className={styles.depth1Frame6} />
      </div>
    </div>
  );
};

export default ProfileScreen;
